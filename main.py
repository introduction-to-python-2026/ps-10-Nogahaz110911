import matplotlib.pyplot as plt

# Display histogram to determine threshold
plt.figure(figsize=(10, 6))
plt.hist(edgeMAG.ravel(), bins=500)
plt.title('Histogram of Edge Magnitudes')
plt.xlabel('Edge Magnitude')
plt.ylabel('Frequency')
plt.show()

# Choose a threshold based on the histogram (example threshold, adjust as needed)
threshold = 20 # This value should be chosen after inspecting the histogram

# Create a binary image
edge_binary = edgeMAG > threshold

print(f"Edge binary image created with threshold: {threshold}")

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Display the binary edge image
plt.figure(figsize=(10, 8))
plt.imshow(edge_binary, cmap='gray')
plt.title('Binary Edge Image')
plt.axis('off') # Hide axes ticks and labels
plt.show()
threshold = 120

# Convert the binary array to a PIL Image and save
# Convert boolean array to uint8 (0 or 255) for saving
edge_image_pil = Image.fromarray((edge_binary * 255).astype(np.uint8))
edge_image_pil.save('my_edges.png')

print("Binary edge image displayed and saved as 'my_edges.png' successfully.")
