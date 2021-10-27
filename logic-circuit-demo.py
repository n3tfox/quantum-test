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
from dimod.reference.samplers import ExactSolver
from dwave.system import DWaveSampler, EmbeddingComposite

import dwavebinarycsp
print("defining circuit\n")
def logic_circuit(a,b,z):
    and1=a and b

    or1= a or b
    not1= not and1
    xor1=or1 and not1
    output1=xor1
    return (output1==z)
print("csp setting var\n")
csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
print("csp adding constraint\n")
csp.add_constraint(logic_circuit, ['a', 'b', 'z'])
print("converting to bqm\n")
# Convert the binary constraint satisfaction problem to a binary quadratic model
bqm = dwavebinarycsp.stitch(csp)
print("printing bqm\n")
print(bqm)
print("making sampler\n")
sampler = EmbeddingComposite(DWaveSampler())
print("making sampleset\n")
sampleset = sampler.sample(bqm, num_reads=10, label='output')
print("printing sampleset\n")

print(sampleset)
