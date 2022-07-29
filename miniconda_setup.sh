#!/bin/zsh

if [ -d "/goinfre" ]; then
  # Take action if $DIR exists. #
  echo "setting MYPATH for school\n"
  export MYPATH="/goinfre/$USER/miniconda3"
else
  echo "setting MYPATH for mac\n"
  export MYPATH="/miniconda3"
fi

if [[ "$(uname)" == "Darwin" ]]; then
	# For MAC
	if [ -e Miniconda3-latest-MacOSX-x86_64.sh ]; then
		echo "Miniconda3 intallation file already exists; continuing..."
	else
		curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
	fi
	sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $MYPATH
elif [[ "$(uname)" == "Linux" ]]; then

	if [ -e "Miniconda3-latest-Linux-x86_64.sh" ]; then
		echo "Miniconda3 intallation file already exists; continuing..."
	else
		curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
	fi
	sh Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH
fi

# For zsh
$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc

# For bash
# $MYPATH/bin/conda init bash
# $MYPATH/bin/conda config --set auto_activate_base false
# source ~/.bash_profile

conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy -y
