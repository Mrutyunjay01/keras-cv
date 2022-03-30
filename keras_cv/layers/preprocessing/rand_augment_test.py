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
from absl.testing import parameterized

from keras_cv import layers


class RandAugmentTest(tf.test.TestCase, parameterized.TestCase):
    @parameterized.named_parameters(
        ("0", 0),
        ("2", 2),
        ("5_5", 5.5),
        ("10", 10.0),
    )
    def test_runs_with_magnitude(self, magnitude):
        rand_augment = layers.RandAugment(magnitude=magnitude)
        xs = tf.ones((2, 512, 512, 3))
        ys = rand_augment(xs)
        self.assertEqual(ys.shape, (2, 512, 512, 3))
