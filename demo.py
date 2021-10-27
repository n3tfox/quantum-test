# Copyright 2021 naru fox
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
import dwavebinarycsp

def logic_circuit(a, b, c, d, z):
    not1 = not b
    or2 = b or c
    and3 = a and not1
    or4 = or2 or d
    and5 = and3 and or4
    not6 = not or4
    or7 = and5 or not6
    return (z == or7)

csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(logic_circuit, ['a', 'b', 'c', 'd', 'z'])

