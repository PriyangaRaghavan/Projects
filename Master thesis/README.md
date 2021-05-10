# Learning Planning Domains Using IoT Data

## Package requirements
    The implementation is done using Python and it requires packages like numpy, pandas, openpyxl and matplotlib

## PDDL planner
   MetricFF planner is used to run the PDDL domain and problem files. 
   Below is the link
   https://fai.cs.uni-saarland.de/hoffmann/metric-ff.html
   
## Structure of the files uploaded

   * source code 
      - "Triaining" folder contains the training files. The dataset has temperature measured in °C,   air-quality in ppm and illuminance in Lux.
      - "outputFiles" folder has Extracted rules and PDDL code outputs.
      - "Evaluation" folder has the intermediate files created which are required for evaluation.
      - When main.py is run it shows the output of the loaded dataset (Dataset with no noise and missing observations is loaded). 
      - To check other outputs, "Training" folder in source code should be replaced with the corresponding training folder from "Dataset and output files" folder.
      - The files in the folder "outputFiles" will be overwritten. It is best to delete the .txt files in "outputFiles" folder  and LearnedPredicates.txt in "Evaluation" folder before loading and running the other dataset. This avoids appending the existing document and obtaining incorrect results.
      - The evaluation results from different dataset are obtained separately and plotted. "plot.py" file has the manually entered values, as the evaluation results are collected separated by loading different dataset.

    * Dataset and output files
      - This folder contains training files for different cases like dataset with different percentage of noise and missing values in observations.
      - It also contains the corresponding output files.

    * PDDL
      - This folder has the handcrafted domain which is used as reference domain.

    * Test problems
      - This folder has the test problems which are used for evaluation.



