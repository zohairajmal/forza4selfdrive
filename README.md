# forza4selfdrive
A self driving car in forza horizon 4.

# How to run

* Run main.py to collect the data, it collects the keys registered with the corresponding position on the lane. Once collected enough data, run balance_data.py to make sure its balanced and size is reduced. After that use train_model.py to train the model *use tensorflowgpu so that it doesnt take days to train). Change the log dir path at end of file to your suitable location. Run tensoreboard from cmd and open it on local host to see the accuracy go up and loss go down. When complete, run test_model.py to see it in action. 



