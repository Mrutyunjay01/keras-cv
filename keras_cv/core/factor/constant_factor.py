# Copyright 2022 The KerasCV Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import tensorflow as tf

from keras_cv.core.factor.factor import Factor


@tf.keras.utils.register_keras_serializable(package="keras_cv")
class ConstantFactor(Factor):
    """ConstantFactor samples the same factor for every call to `sample()`.

    This is useful in cases where a user wants to always ensure that an augmentation
    layer performs augmentations of the same strength.

    Args:
        value: the value to return from `sample()`.

    Usage:
    ```python
    constant_factor = keras_cv.core.ConstantFactor(0.5)
    random_sharpness = keras_cv.layers.RandomSharpness(factor=constant_factor)
    # random_sharpness will now always use a factor of 0.5
    ```
    """

    def __init__(self, value):
        self.value = value

    def sample(self):
        return self.value

    def get_config():
        return {"value": self.value}