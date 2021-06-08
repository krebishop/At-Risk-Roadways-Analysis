The purpose of this code is to streamline the indentification of potential at risk roadways in burn areas within the state of Oregon. The risk factor
being identified is stream proximity. While most development must maintain around 100ft "buffer" on either side of the stream for higher flow water sources, it
has been researched that this area may need to be increased by 8x in recent burn zones. This led to the parameters of approx. 250m for high flow streams, 
150m for medium flow, and 50m for low flow streams.

Three main inputs have been taken to create a single output road ways feature class. The streams and roadways feature classes are within the geodatabase referenced
for the work environment. The fire boundary is identied by the user. It is recommended that this is a shapefile with a single boundary, and example fire boundary shapfile
has been included for a test with the script and data. The input boundary is used to intersect with the streams layer. This intersected streams layer is used to create 
three buffer zones of the distances noted above. These buffers are joined into one feature and are used as a clip template for the roadways feature class. The final
feature class ouput will be the user named output in the workspace environment. 

Overwritting has been allowed within the code to allow for multiple runs of the script without it erroring out. The user input for the outputs variable name though does allow
for multiple outputs to exist in the workspace, so that different areas can be ran one after the other with the script. The environment will need to be set to your preferred
workspace, and the data in the included gdb should be used for the analysis. 

Note: This code and data are best suited for areas within the State of Oregon. The script was created in Spyder and ran with ArcGIS Pro 2.7.0

Coordinate System: The streams and roadways feature classes utilize the same PCS. NAD 1983 Oregon Statewide Lambert (Intl Feet)

Contact Information: Kaitlyn Bishop, bishopka@oregonstate.edu