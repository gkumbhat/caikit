# Copyright The Caikit Authors
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
"""
This module holds the Task definitions for all common NLP tasks
"""

# Standard
from typing import Iterable

# Local
from ...core import TaskBase, task
from .data_model.classification import (
    ClassificationResult,
    ClassifiedGeneratedTextResult,
    ClassifiedGeneratedTextStreamResult,
    TokenClassificationResult,
    TokenClassificationStreamResult,
)
from .data_model.text import TokenizationResult, TokenizationStreamResult
from .data_model.text_generation import GeneratedTextResult, GeneratedTextStreamResult


@task(
    unary_parameters={"text": str},
    unary_output_type=GeneratedTextResult,
    streaming_output_type=Iterable[GeneratedTextStreamResult],
)
class TextGenerationTask(TaskBase):
    """The Text Generation Task is responsible for taking input prompting text
    and generating additional text from that prompt.
    """


@task(
    required_parameters={"text": str},
    output_type=ClassificationResult,
)
class TextClassificationTask(TaskBase):
    pass


@task(
    unary_parameters={"text": str},
    streaming_parameters={"text_stream": Iterable[str]},
    unary_output_type=TokenClassificationResult,
    streaming_output_type=Iterable[TokenClassificationStreamResult],
)
class TokenClassificationTask(TaskBase):
    pass


@task(
    unary_parameters={"text": str},
    streaming_parameters={"text_stream": Iterable[str]},
    unary_output_type=TokenizationResult,
    streaming_output_type=Iterable[TokenizationStreamResult],
)
class TokenizationTask(TaskBase):
    pass


@task(
    unary_parameters={"text": str},
    unary_output_type=ClassifiedGeneratedTextResult,
    streaming_output_type=Iterable[ClassifiedGeneratedTextStreamResult],
)
class ClassificationWithTextGenerationTask(TaskBase):
    """The Classification with Text Generation Task is responsible for taking
    input prompting text, generating additional text from that prompt and classifying
    the generated text based on detectors.
    """
