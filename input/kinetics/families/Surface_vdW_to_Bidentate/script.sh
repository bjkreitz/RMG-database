#!/usr/bin/env bash
#SBATCH --job-name=Surface_vdW_to_Bidentate
#SBATCH --time=1:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem=60GB
#SBATCH --account=cfgoldsm-condo
#SBATCH --mail-type=END
#SBATCH --mail-user=bjarne_kreitz@brown.edu

module load anaconda/2020.02
source /gpfs/runtime/opt/anaconda/2020.02/etc/profile.d/conda.sh
conda activate /users/bkreitz1/anaconda/rmg_env

python uq.py

