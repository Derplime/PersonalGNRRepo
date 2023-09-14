#!/usr/bin/zsh

# Case statement to execute the corresponding Python script
case $1 in
  1)
    python_script="rf_flowgraph_1.py"
    # Kill any currently running flowcharts if needed
    #TODO add original script as well
    pkill -f rf_flowgraph_2.py
    ;;
  2)
    python_script="rf_flowgraph_2.py"
    # Kill any currently running flowcharts if needed
    pkill -f rf_flowgraph_1.py
    ;;
  *) # Default case
    echo "Invalid input. No Python script to run."
    exit 1
    ;;
esac

# Check if Python script exists and run it
if [ -e "$python_script" ]; then
  echo "Running $python_script..."
  # Run the flowgraph script
  ./"$python_script"
else
  echo "Python script $python_script does not exist."
fi
