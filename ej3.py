import numpy as np

def calcular_tensor_deformaciones(desplazamientos_nodales):
    """
    Calcula el tensor de deformaciones para un elemento finito tetraédrico dado su matriz de desplazamientos nodales.

    Args:
    - desplazamientos_nodales: Matriz de desplazamientos nodales del elemento tetraédrico. Debe ser una matriz 4x3, donde cada fila representa los desplazamientos nodales para un nodo.

    Returns:
    - tensor_deformaciones: Tensor de deformaciones para el elemento tetraédrico. Es una matriz 3x3.
    """
    # Coordenadas de los nodos
    x = desplazamientos_nodales[:, 0]
    y = desplazamientos_nodales[:, 1]
    z = desplazamientos_nodales[:, 2]
    
    # Matriz de gradiente de desplazamientos
    grad_u = np.zeros((3, 3))
    
    # Calcular derivadas parciales de los desplazamientos con respecto a las coordenadas espaciales
    grad_u[0, 0] = np.gradient(x)[0]
    grad_u[1, 0] = np.gradient(y)[0]
    grad_u[2, 0] = np.gradient(z)[0]
    grad_u[0, 1] = np.gradient(x)[1]
    grad_u[1, 1] = np.gradient(y)[1]
    grad_u[2, 1] = np.gradient(z)[1]
    grad_u[0, 2] = np.gradient(x)[2]
    grad_u[1, 2] = np.gradient(y)[2]
    grad_u[2, 2] = np.gradient(z)[2]
    
    # Calcular el tensor de deformaciones
    tensor_deformaciones = 0.5 * (grad_u + np.transpose(grad_u))
    
    return tensor_deformaciones

# Ejemplo de uso
desplazamientos_nodales = np.array([[0.1, 0.2, 0.3],
                                     [0.2, 0.3, 0.4],
                                     [0.3, 0.4, 0.5],
                                     [0.4, 0.5, 0.6]])

tensor_deformaciones = calcular_tensor_deformaciones(desplazamientos_nodales)
print("Tensor de deformaciones:")
print(tensor_deformaciones)
