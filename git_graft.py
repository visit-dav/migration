#######################################
# git_graft.py
#######################################

import glob
import shutil

from os.path import join as pjoin

from general_utils import *
from svn_utils import *
from git_utils import *


def git_graft_initial_setup():
    print "[checking rc git svn repos]"
    svn_check_rc_git_svn_repos()
    print "[setting up new git repo]"
    git_setup_new_repo()
    print "[connecting git svn remotes]"
    git_connect_git_svn_remotes()

def git_graft_setup_develop():
    print "[setting up git develop branch]"
    git_setup_develop()

def git_graft_create_rc_branches():
    # for each rc, create rc branch
    rcs = svn_ls_rc_branches()
    for rc in rcs:
        if not rc.startswith("1.") and os.path.isdir( git_svn_rc_checkout_dir(rc)):
            print "[creating rc branch %s]" % rc
            git_create_rc_branch(rc)

def generate_rc_branch_patches():
    # for each rc gen a patch with all of their commits
    rcs = svn_ls_rc_branches()
    for rc in rcs:
      print "[generating rc branch patch for %s]" % rc
      git_generate_rc_branch_patch(rc)

def git_graft_tag_releases():
    # for each release, create squashed commit to master
    rcs = svn_ls_rc_branches()
    for rc in rcs:
      if not rc.startswith("1."):
          print "[tagging releases off of rc %s]" % rc
          for release in svn_release_tags_for_rc(rc):
              print "[tagging release %s]" % release
              git_tag_release(release)

def git_graft():
    #generate_rc_branch_patches()
    #git_graft_initial_setup()
    #git_graft_setup_develop()
    #git_graft_create_rc_branches()
    #git_graft_tag_releases()
    git_final_cleaup()

if __name__ == "__main__":
    git_graft()




