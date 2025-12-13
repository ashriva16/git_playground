import numpy as np
import torch
from sklearn.model_selection import KFold


def create_bootstraped_data(dataset, n_bootstrap=10):
    """
    Generate bootstrapped datasets.

    Parameters:
    n_bootstrap: int
        The number of bootstrapped datasets to create.

    Returns:
    List[Tuple[Tensor, Tensor]]
        A list of tuples, each containing the bootstrapped x_data and y_data tensors.
    """
    bootstrapped_datasets = []
    if n_bootstrap == 0:
        bootstrapped_datasets.append(dataset)
    else:
        n_samples = len(dataset.x_data)
        for _ in range(n_bootstrap):
            # Sample indices with replacement
            indices = np.random.choice(n_samples, n_samples, replace=True)
            trainsubset = torch.utils.data.Subset(dataset, indices)
            # Append bootstrapped (x_data, y_data) as a tuple
            bootstrapped_datasets.append(trainsubset)

    return bootstrapped_datasets


def create_crossval_data(dataset, folds=10):
    """
    Generate bootstrapped datasets.

    Parameters:
    n_bootstrap: int
        The number of bootstrapped datasets to create.

    Returns:
    List[Tuple[Tensor, Tensor]]
        A list of tuples, each containing the bootstrapped x_data and y_data tensors.
    """
    crossval_datasets = []
    if folds == 0:
        crossval_datasets.append(dataset)
    else:
        kfold = KFold(n_splits=folds, shuffle=True)
        for _, (train_ids, _) in enumerate(kfold.split(dataset)):
            # Sample indices with replacement
            trainsubset = torch.utils.data.Subset(dataset, train_ids)
            crossval_datasets.append(trainsubset)

    return crossval_datasets
