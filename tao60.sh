#!/bin/bash
#
#$ -V
#$ -cwd
#$ -j y
#$ -S /bin/bash
# #$ -q marvin.q,all.q,lowmemory.q,single.q,highmemory.q
#$ -q all.q,lowmemory.q,single.q,highmemory.q
#$ -pe multi 128
#$ -l h_rt=00:10:00
#$ -l s_rt=00:10:00
#$ -l h_vmem=1G
#
mpirun -np ${NSLOTS} ./a.out $((${NSLOTS}*1000))
