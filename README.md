# forza4selfdrive
-ScreebGrab.py ----> python .\ScreenGrab.py 
Captures the screen into a 800x 600 window. Fixed color conversion issue from bgr to rgb.
-Added images of progress
-Run main.py to collect the data, it collects the keys registered with the corresponding position on the lane. Once collected enough data, run balance_data.py to make sure its balanced and size is reduced. After that use train_model.py to train the model *use tensorflowgpu so that it doesnt take days to train). Change the log dir path at end of file to your suitable location. Run tensoreboard from cmd and open it on local host to see the accuracy go up and loss go down. When complete, run test_model.py to see it in action. 
-using alexnet model to train model.
