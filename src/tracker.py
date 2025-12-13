import logging
import os

import torch
from tensorboardX import SummaryWriter
from torchinfo import summary


def save_checkpoint(model, optimizer, scheduler, epoch, save_path, best=False, hparams=None):
    """Save model state."""
    os.makedirs(save_path, exist_ok=True)

    checkpoint = {
        "model_state_dict": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "optimizer_name": type(optimizer).__name__,
        "scheduler": scheduler.state_dict() if scheduler else None,
        "epoch": epoch,
        "initial_hparams": hparams,
    }
    torch.save(
        checkpoint, os.path.join(save_path, "best_model.pth" if best else f"checkpoint_{epoch}.pth")
    )


class ExperimentTracker:
    """Creates folder, setup logger and tensorboard writer

    Args:
        model (torch module): _description_

    Returns:
        dict: returns tensorboard writer and file handler
    """

    def __init__(self, display=True):
        self.tensorboard = None

        # logger setup
        self.file = logging.getLogger(__name__)
        self.file.setLevel(logging.DEBUG)
        self.file.handlers = []  # Clear previous handlers to avoid duplicate logs

        self.formatter = logging.Formatter("%(message)s")

        if display:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(self.formatter)
            self.file.addHandler(console_handler)

    def _setup_log_directory(self, config_dict, model, name_suffix_list):
        directory = config_dict["result_dir"]
        # Result directory setup --------------------------------
        if name_suffix_list is not None:
            name_suffix_str = "_".join(map(str, name_suffix_list))
            config_dict["name_suffix_str"] = name_suffix_str
            result_dir = os.path.join(directory, f"{model.get_model_name()}_{name_suffix_str}")
        else:
            result_dir = os.path.join(directory, model.get_model_name())

        # Create if result_dir does not exsit
        os.makedirs(result_dir, exist_ok=True)

        relog_flag = ("run_ver" not in config_dict) or (config_dict["run_ver"] is None)
        if relog_flag:
            # creating new run folder
            listdir = os.listdir(result_dir)
            config_dict["run_ver"] = "run" + str(len(listdir))

            log_path = os.path.join(result_dir, config_dict["run_ver"])
            os.makedirs(log_path, exist_ok=True)
            config_dict["log_path"] = log_path

        return relog_flag

    def _log_init_setup(self, config_dict, model):
        # Log initial info --------------------------------------
        self.file.info(summary(model, verbose=0, col_width=16))

        # Create a dummy input tensor
        dummy_input = torch.randn(1, *config_dict["data_shape"])
        self.tensorboard.add_graph(model, dummy_input)

        # Log hyperparameters -------------------------------------
        self.file.info("\nTrain Settings")
        self.file.info("\n %s", "==" * 28)
        self.file.info("".join([f"{key}:\t{value}\n" for key, value in config_dict.items()]))
        self.file.info("%s", "==" * 28)

    def configure_log(self, config_dict, model, name_suffix_list=None, log_to_file=True):
        relog_flag = self._setup_log_directory(config_dict, model, name_suffix_list)

        # Add logfile handler -----------------------------------
        if log_to_file:
            logfilename = os.path.join(config_dict["log_path"], "train.log")
            file_handler = logging.FileHandler(logfilename)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(self.formatter)
            self.file.addHandler(file_handler)

        # Tensorboard write setup -------------------------------
        tensorboard_dir_path = os.path.join(config_dict["log_path"], "tb")
        self.tensorboard = SummaryWriter(log_dir=tensorboard_dir_path)

        if relog_flag:
            self._log_init_setup(config_dict, model)

    def log_model_params(self, model, epoch):
        """Logs model parameters and gradients to TensorBoard."""

        for name, param in model.named_parameters():
            self.tensorboard.add_histogram(name, param.detach().cpu().numpy(), epoch)

        # to observe vanishing gradients
        for name, param in model.named_parameters():
            if param.grad is not None:
                self.tensorboard.add_histogram(name + "_grad", param.grad.norm().item(), epoch)

    def log_results(self, loss_dict, epoch, tag=""):
        """Logs training and validation metrics to TensorBoard and console."""

        exc = f"Epoch: {epoch}\t" + "\t\t".join(
            [f"{key}: {value:.6f}" for key, value in loss_dict.items()]
        )

        self.file.info(exc)
        self.tensorboard.add_scalars(tag, loss_dict, epoch)
