import os
import trimesh

# Define the function to scale STL files
def scale_stl(file_path, scale_factor):
    # Load the STL file
    mesh = trimesh.load(file_path)
    
    # Create a copy of the original mesh for comparison
    original_mesh = mesh.copy()
    
    # Calculate the scaling transformation matrix
    scale_matrix = trimesh.transformations.scale_matrix(scale_factor)
    
    # Apply the scaling transformation
    mesh.apply_transform(scale_matrix)
    
    # Save the transformed STL file
    new_file_path = file_path[:-4] + "_scaled.stl"
    mesh.export(new_file_path)
    
    # Create a scene and add both original and scaled mesh
    scene = trimesh.Scene([original_mesh, mesh])
    
    # Set different colors for original and scaled mesh for distinction
    original_mesh.visual.face_colors = [255, 0, 0, 100]  # Red, semi-transparent
    mesh.visual.face_colors = [0, 255, 0, 100]  # Green, semi-transparent
    
    # Show the scene
    scene.show()

    print(f"File has been scaled and saved as: {new_file_path}")

# Function to run tests
def test_scale_stl():
    # Test file path
    test_file_path = "./speaker/speaker_asm.stl"  # Replace with the actual path of your STL file
    # test_file_path = "~/catkin_ws/src/acoustic_measurement/config/environments/turntable_with_model.stl"  # Replace with the actual path of your STL file

    # Test scaling up
    scale_factor = 0.001  # Double the size
    print("Testing scale up by factor of " + str(scale_factor))
    scale_stl(test_file_path, scale_factor)


# Run the test function
if __name__ == "__main__":
    test_scale_stl()

