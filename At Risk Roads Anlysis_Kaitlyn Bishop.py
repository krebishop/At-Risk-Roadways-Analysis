#########
# At Risk Roads Analysis_Kaitlyn Bishop.py
# Created May 20, 2021
#
# Purpose: Streamlines a roads intersection analysis with stream buffer zones and a user input burn area
#################################################################


# imports module for ArcGIS functions and classes
import arcpy

# Sets the current worskpace, which will need to be changed to match were the streams and roads data are located. The workspace is where data are
# located and new feature classes will be added to. Overwritting of duplicates in the workspace is allowed.
arcpy.env.workspace = "C:/Users/krebi/OneDrive - Oregon State University/Desktop/GEOG 562/Final project/Final project Data/Default.gdb"
arcpy.env.overwriteOutput = True

# Creates variables for the streams and roadways feature classes in our workspace
streamsAll = "streams"
roadsAll = "roadways"

# Creates a loop statement to allow for user input and checks the input for existence 
# and that it is a polygon feature class. If these conditions are met, a prompt is given to allow the user
# to specify the output variable name. It is noted that duplicate names will be overwritten.
while True:
    print("Type full pathway for fire boundary feature class in Oregon. Please use forward slashes.")
    fireBound = input()
    roadsClip = input("Name ouput feature to be created in environment. Take care to not create duplicate names.")
    if arcpy.Exists(fireBound) and arcpy.da.Describe(fireBound)["shapeType"] == "Polygon":
        print("Name ouput feature to be created in environment. Duplicate names will be overwritten.")
        roadsClip = input
        break
    else:
        print("Feature class not found or is not polygon shapetype")

# error exception class to hold code and produce an output for the exception that occured rather
try:

    # Creates a new featureclass for the intersection of the user input fire boundary and 
    # the streams layer, and displays that the process has been completed
    streamIntersect = "fireBound_streams"
    arcpy.Intersect_analysis([fireBound, streamsAll], streamIntersect)
    print("Streams clipped to fire boundary input")

    # Creates new feature classes for high flow, medium flow, and low flow streams within
    # the fire boundary streams featureclass, and ensures that the selection clause is formatted
    # properly, since the fire boundaries stream featureclass is in the workspace geodatabase
    highFlow = "high_flow_streams"
    mediumFlow = "medium_flow_streams"
    lowFlow = "low_flow_streams"
    delimfield = arcpy.AddFieldDelimiters(streamIntersect,"Fpasize")
    whereHigh = delimfield + " = 'Large'"
    whereMedium = delimfield + " = 'Medium'"
    whereLow = delimfield + " = 'Low'"
    arcpy.Select_analysis(streamIntersect, highFlow, whereHigh)
    arcpy.Select_analysis(streamIntersect, mediumFlow, whereMedium)
    arcpy.Select_analysis(streamIntersect, lowFlow, whereLow)

    # Creates a 250m buffer for high flow streams, a 150m buffer for medium flow streams, 
    # and a 50m buffer for low flow streams, and displays that the buffers have been created 
    # for each flow type
    highBuffer = "high_flow_streams_250m"
    medBuffer = "medium_flow_streams_150m"
    lowBuffer = "low_flow_streams_50m"
    bufferDist_high = "250 meters"
    bufferDist_med = "150 meters"
    bufferDist_low = "50 meters"
    arcpy.Buffer_analysis(highFlow, highBuffer, bufferDist_high, "","","ALL")
    arcpy.Buffer_analysis(mediumFlow, medBuffer, bufferDist_med, "","","ALL")
    arcpy.Buffer_analysis(lowFlow, lowBuffer, bufferDist_low, "","","ALL")
    print("Buffer zones created for streams based on flow type")
    
    # Combines all the flow buffers into a new featureclass, and displays that the buffers have been
    # unioned into one new featureclass
    unionFeatures = [highBuffer, medBuffer, lowBuffer]
    streamUnion = "stream_buffer_areas"
    arcpy.Union_analysis(unionFeatures, streamUnion)
    print("Stream buffers union created.")

   # Uses the combined buffer featureclass to select and export the roadways within the buffer areas
   # into a new feature class for the high risk roadways, which was specified by the user
    arcpy.Clip_analysis(roadsAll, streamUnion, roadsClip)

    # Displays that our final feature class for roadways at risk from streams in the burn area
    # has been created.
    print("High risk roadways feature class created.")

# exception statement for when a geoprocessing tool encounters an error that prints the error message
# rather than immediately stopping the running of the script
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))

# exception statement for when an error occurs that prints that an error has been encountered, not
#not related to geoprocessed, rather than immediately stopping the running of the script
except:
    print("A non-geoprocessing error has occured")
    
