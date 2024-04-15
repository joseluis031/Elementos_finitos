import vtk
import numpy as np

# Supongamos que tienes resultados de presiones y desplazamientos en matrices numpy
# Por ejemplo:
pressures = np.random.rand(10, 10, 10).astype(np.float32)  # Convertir a flotante de precisión simple
displacements = np.random.rand(10, 10, 10, 3).astype(np.float32)  # Convertir a flotante de precisión simple

# Crear un objeto vtkImageData para las presiones
pressure_data = vtk.vtkImageData()
pressure_data.SetDimensions(pressures.shape)
pressure_data.SetOrigin(0, 0, 0)
pressure_data.SetSpacing(1, 1, 1)

# Convertir las presiones a un vtkFloatArray
pressure_array = vtk.vtkFloatArray()
pressure_array.SetNumberOfComponents(1)
pressure_array.SetNumberOfTuples(pressures.size)
pressure_array.SetArray(pressures.flatten(), pressures.size, 1)

# Asignar el array de presiones al vtkImageData
pressure_data.GetPointData().SetScalars(pressure_array)

# Crear un objeto vtkImageData para los desplazamientos
displacement_data = vtk.vtkImageData()
displacement_data.SetDimensions(displacements.shape[:-1])  # Eliminar la dimensión de componentes
displacement_data.SetOrigin(0, 0, 0)
displacement_data.SetSpacing(1, 1, 1)

# Convertir los desplazamientos a un vtkFloatArray
displacement_array = vtk.vtkFloatArray()
displacement_array.SetNumberOfComponents(3)  # 3 componentes para x, y, z
displacement_array.SetNumberOfTuples(displacements.size // 3)
displacement_array.SetArray(displacements.flatten(), displacements.size, 1)

# Asignar el array de desplazamientos al vtkImageData
displacement_data.GetPointData().SetVectors(displacement_array)

# Guardar los datos en formato VTK
writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName("structural_results.vti")
writer.SetInputData(pressure_data)
writer.Write()

# Guardar los desplazamientos en un archivo separado (opcional)
writer.SetFileName("displacement_results.vti")
writer.SetInputData(displacement_data)
writer.Write()
