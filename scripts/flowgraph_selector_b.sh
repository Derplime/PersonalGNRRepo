#!/usr/bin/bash

# Execute the corresponding Python script
python_script="rf_flowgraph_2.py"

# Kill any currently running flowcharts if needed
pkill -f ../flowgraphs/rf_flowgraph_1.py
pkill -f ../flowgraphs/rf_flowgraph_2.py

# Check if Python script exists and run it
if [ -e ../flowgraphs/"$python_script" ]; then
  echo "Running $python_script..."
  # Run the flowgraph script
  ../flowgraphs/"$python_script"
else
  echo "Python script $python_script does not exist."
fi
