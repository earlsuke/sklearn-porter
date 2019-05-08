# -*- coding: utf-8 -*-

from typing import Union, Optional, Callable
from logging import Logger, ERROR

from sklearn.neural_network.multilayer_perceptron \
    import MLPRegressor as MLPRegressorClass

from sklearn_porter.EstimatorInterApiABC import EstimatorInterApiABC
from sklearn_porter.estimator.Templater import Templater
from sklearn_porter.utils import get_logger


class MLPRegressor(EstimatorInterApiABC, Templater):
    """
    Class to extract model data and port a MLPRegressor.

    See also
    --------
    http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html
    """
    estimator = None  # type: MLPRegressorClass

    def __init__(
            self,
            estimator: MLPRegressorClass,
            logger: Union[Logger, int] = ERROR
    ):
        self.logger = get_logger(__name__, logger=logger)

        self.estimator = est = estimator  # alias
        self.estimator_name = self.__class__.__qualname__
        self.logger.info('Create specific estimator `%s`.', self.estimator_name)

        # TODO: Export and prepare model data from estimator.

    def port(
            self,
            method: str = 'predict',
            to: Union[str] = 'java',  # language
            with_num_format: Callable[[object], str] = lambda x: str(x),
            with_class_name: Optional[str] = None,
            with_method_name: Optional[str] = None
    ) -> str:
        temps = self.load_templates(self.estimator_name, language=to)

        print(temps.keys())

        return str(self.estimator)