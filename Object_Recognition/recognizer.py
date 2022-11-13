# importing the required library  
from imageai.Detection import ObjectDetection  

  
# instantiating the class  
recognizer = ObjectDetection()  

# defining the paths  
path_model = "./Models/yolo-tiny.h5"  
path_input = "./Input/images.jpg"  
path_output = "./Output/newimage.jpg"  
  
# using the setModelTypeAsTinyYOLOv3() function  
recognizer.setModelTypeAsTinyYOLOv3()  
# setting the path of the Model  
recognizer.setModelPath(path_model)  
# loading the model  
recognizer.loadModel()  
# calling the detectObjectsFromImage() function  
recognition = recognizer.detectObjectsFromImage(  
    input_image = path_input,  
    output_image_path = path_output  
    )  
  
# iterating through the items found in the image  
#for eachItem in recognition:  
    #print(eachItem["name"] , " : ", eachItem["percentage_probability"])

#Jakes Carbonemmions conversion

#example 


objectList = ['pizza','bicyle', 'cow', 'pig/pork', 't-shirt', 'laptop', 'phone', 'shoes', 'chicken', 'person' ]
emmisionList = [5.1, 96, 36, 1.8, 6.75, 422.5, 63, 14, 12.27, 14515 ]

def objcetCarbonFootPrint(object, footprint):
    print(f"{object} has a footprint of {float(footprint)} kgs")

for eachItem in recognition:
    object = eachItem
    index = objectList.index(object)
    footfprint = emmisionList(index)
    objcetCarbonFootPrint(object, footfprint)

    
