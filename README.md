# Neovim Startup Time Analysis

This project analyzes the startup time of Neovim and visualizes the loading times of plugins managed by Packer.

## Project Overview

The project consists of two main files:

- `neovim_startup.py`: Python script used for visualization and analysis.
- `profiler.sh`: Shell script used to prepare the raw data of Neovim startup time.

## Getting Started

To use this project, follow the steps below:

1. Clone the repository:

    ```shell
   git clone https://github.com/AnupPainuly/neovim-startup-analysis.git 
   cd neovim-startup-analysis

    ```
1. Run the profiler.sh script to gather the raw data of Neovim startup time. Make sure you have Neovim installed.

    ```shell

    ./profiler.sh

    ```
1. Run the neovim_startup.py script to visualize the loading times of Neovim plugins managed by Packer.

    ```shell
    python neovim_startup.py
    ```

## Dependencies

The project has the following dependencies:

- Python 3.x
- pandas library
- Matplotlib library (for data visualization)
- seaborn(optional)



Please ensure that you have Python 3.x installed on your system. You can check the version of Python installed by running the following command in your terminal:

    ```shell
    python --version 
    ```
