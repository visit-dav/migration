#!/bin/bash
#SBATCH -N 1
#SBATCH -J visit_svn_git_clone_all
#SBATCH -t 12:00:00
#SBATCH -A wbronze
#SBATCH -o m.out.svn_git_clone_all.txt
date
cd  /usr/workspace/wsa/cyrush/2018.06.visit.svn.migrate/migration
python svn_git_clone_branches.py
date




