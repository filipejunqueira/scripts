#!/bin/bash

CWD=$(pwd)
CORES=${1:-24}

cat > jobscript.job << EOF
#!/bin/bash -l

# Force bash as the executing shell.
#$ -S /bin/bash

#$ -P Gold
#$ -A KCL_Kantorovich

# Select the MPI parallel environment and 24 processes.
#$ -pe mpi $CORES

# Request wallclock time (format hours:minutes:seconds).
#$ -l h_rt=00:10:00

# Request RAM per process (it is per CORE and not per JOB)
#$ -l mem=1G

# Request gigabytes of TMPDIR space per node (default is 10 GB)
#$ -l tmpfs=10G

# Set the name of the job.
#$ -N vaspJob

# Set the working directory 
#$ -wd $CWD

# To restrict a job to newer nodes only ( uncomment)
# #$ -ac allow=LMNOPQSTU

# cd $CWD

VASP_STD=/home/mmm0540/src/vasp.5.4.1/vasp_std
VASP_GAM=/home/mmm0540/src/vasp.5.4.1/vasp_gam
BIN_VASP=\$VASP_STD

gerun \$BIN_VASP
EOF
