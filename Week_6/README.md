# Week 6 Assignment: ANN vs. CNN Comparison

This directory contains the Jupyter Notebooks and documentation for the Week 6 assignment. The goal of this assignment was to build, train, and compare the performance of simple Artificial Neural Networks (ANNs) and Convolutional Neural Networks (CNNs) on two distinct datasets: the MNIST dataset of handwritten digits and the Cat-vs-Dog dataset of real-world images.

## Project Deliverables

### 1. Implementation Code & Training Logs
The complete implementation, including model architectures, data preprocessing, training loops, and results, can be found in the following notebooks:

*   **[CNN_ANN_MNIST.ipynb](./CNN_ANN_MNIST.ipynb)**: Contains the code and analysis for the MNIST dataset comparison.
*   **[CNN_ANN_Cat-vs-Dog.ipynb](./CNN_ANN_Cat-vs-Dog.ipynb)**: Contains the code and analysis for the Cat-vs-Dog dataset comparison.

### 2. Summary of Architectures and Findings

#### Part 1: MNIST Dataset (Simple Classification)
*   **ANN Architecture**: A simple network consisting of a `Flatten` layer to convert 28x28 images into a 1D vector, followed by a `Dense` hidden layer (128 neurons, ReLU), and a `Dense` output layer (10 neurons, Softmax).
*   **CNN Architecture**: A basic CNN with a `Conv2D` layer (32 filters), a `MaxPooling2D` layer, a `Flatten` layer, a `Dense` hidden layer (128 neurons, ReLU), and a `Dense` output layer (10 neurons, Softmax).
*   **Results & Comparison**:
    *   **ANN Test Accuracy**: `97.74%`
    *   **CNN Test Accuracy**: `98.64%`
    *   **Conclusion**: The CNN slightly outperformed the ANN. This demonstrates that even for a simple, standardized dataset like MNIST, the CNN's ability to understand spatial features provides a performance advantage.

#### Part 2: Cat-vs-Dog Dataset (Complex Binary Classification)
*   **ANN Architecture**: A network with a `Rescaling` and `Flatten` layer for the 150x150x3 images, a `Dense` hidden layer (128 neurons, ReLU), and a `Dense` output layer (1 neuron, Sigmoid). This model had over 8.6 million parameters.
*   **CNN Architecture**: A deeper CNN with a `Rescaling` layer, two blocks of `Conv2D` and `MaxPooling2D` layers (32 and 64 filters, respectively), followed by `Flatten`, `Dense` (128 neurons), and `Dense` output layers (1 neuron, Sigmoid).
*   **Results & Comparison**:
    *   **ANN Test Accuracy**: `57.30%`
    *   **CNN Test Accuracy**: `69.00%`
    *   **Conclusion**: The performance difference was dramatic. The ANN, with its massive, unstructured hidden layer, failed to learn meaningful patterns and performed only slightly better than a random guess. The CNN, despite also having many parameters, successfully learned features and performed significantly better. This starkly illustrates that for complex, real-world image data, a CNN is a necessary tool.

### 3. Use of Callbacks and Challenges
*   **Callbacks**: Both `EarlyStopping` and `ModelCheckpoint` were used in all training jobs. `EarlyStopping` proved essential, as it prevented the models from overfitting and saved significant training time by halting the process when validation loss stopped improving. `ModelCheckpoint` ensured that the best-performing version of each model was saved and used for the final evaluation.
*   **Challenges**: The main challenge was the high computational complexity of the Cat-vs-Dog dataset. The ANN, in particular, was overwhelmed by the high-dimensional input and failed to train effectively. For the CNN, the challenge was the longer training time per epoch, which was managed effectively by the use of callbacks.

### 4. How to Run the Code
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/juni2003/Buildable-ML-DL-Fellowship.git
    cd Buildable-ML-DL-Fellowship/Week\ 6
    ```
2.  **Install Dependencies:** Ensure you have TensorFlow and other required libraries installed.
    ```bash
    pip install tensorflow
    ```
3.  **Run Jupyter Notebook:** Launch Jupyter and open either of the `.ipynb` files to review the code and execute the cells.
    ```bash
    jupyter notebook
    ```
The notebooks will automatically download the required datasets the first time they are run.
