# Copyright 2021 Zilliz. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List

from towhee.engine.operator_runner.runner_base import RunnerBase
from towhee.errors import OpIOTypeError


class FlatMapRunner(RunnerBase):
    """
    FlatMap, one input multiple outputs.
    """

    def _set_outputs(self, output: List[any]):
        if not isinstance(output, list):
            raise OpIOTypeError("Flatmap operator's output must be a list, not a {}".format(type(output)))

        for data in output:
            self._writer.write(data)
