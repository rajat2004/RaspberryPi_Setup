#!/bin/bash

echo "Begining by updating and upgrading your OS"

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  echo "Linux Platform Detected"
  sudo apt-get update
  sudo apt-get upgrade
  echo "Installing sshpass"
  sudo apt-get install sshpass

elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Mac OS Platform Detected"
  # Check if Homebrew is installed
  which -s brew
  if [[ $? != 0 ]] ; then
    echo "Installing Homebrew"
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  else
    echo "Homebrew Detected"
    echo "Updating Brew"
    brew update
  fi

  # Check if sshpass is Installed

  if brew ls --versions sshpass > /dev/null; then
    echo "The package is installed"
  else
    brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
  fi


else
  echo "This script supports only UNIX, LINUX"
  echo "Exiting script"
  exit 1
fi

echo "Installing magic wormhole"
pip install magic-wormhole

echo "Script is finished."
