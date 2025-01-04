{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting sklearn\n",
      "  Using cached sklearn-0.0.post12.tar.gz (2.6 kB)\n",
      "  Preparing metadata (setup.py): started\n",
      "  Preparing metadata (setup.py): finished with status 'error'\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  error: subprocess-exited-with-error\n",
      "  \n",
      "  × python setup.py egg_info did not run successfully.\n",
      "  │ exit code: 1\n",
      "  ╰─> [15 lines of output]\n",
      "      The 'sklearn' PyPI package is deprecated, use 'scikit-learn'\n",
      "      rather than 'sklearn' for pip commands.\n",
      "      \n",
      "      Here is how to fix this error in the main use cases:\n",
      "      - use 'pip install scikit-learn' rather than 'pip install sklearn'\n",
      "      - replace 'sklearn' by 'scikit-learn' in your pip requirements files\n",
      "        (requirements.txt, setup.py, setup.cfg, Pipfile, etc ...)\n",
      "      - if the 'sklearn' package is used by one of your dependencies,\n",
      "        it would be great if you take some time to track which package uses\n",
      "        'sklearn' instead of 'scikit-learn' and report it to their issue tracker\n",
      "      - as a last resort, set the environment variable\n",
      "        SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True to avoid this error\n",
      "      \n",
      "      More information is available at\n",
      "      https://github.com/scikit-learn/sklearn-pypi-package\n",
      "      [end of output]\n",
      "  \n",
      "  note: This error originates from a subprocess, and is likely not a problem with pip.\n",
      "error: metadata-generation-failed\n",
      "\n",
      "× Encountered error while generating package metadata.\n",
      "╰─> See above for output.\n",
      "\n",
      "note: This is an issue with the package mentioned above, not pip.\n",
      "hint: See above for details.\n"
     ]
    }
   ],
   "source": [
    "!pip install sklearn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "K_Mean.__init__() got an unexpected keyword argument 'n_cluster'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[30], line 13\u001b[0m\n\u001b[0;32m     10\u001b[0m X, y \u001b[38;5;241m=\u001b[39m make_blobs(n_samples\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m500\u001b[39m, centers\u001b[38;5;241m=\u001b[39mcentroids, random_state\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m2\u001b[39m, n_features\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m2\u001b[39m, cluster_std\u001b[38;5;241m=\u001b[39mcluster_std)\n\u001b[0;32m     12\u001b[0m \u001b[38;5;66;03m# Initialize and use the K_Mean class\u001b[39;00m\n\u001b[1;32m---> 13\u001b[0m km \u001b[38;5;241m=\u001b[39m \u001b[43mK_Mean\u001b[49m\u001b[43m(\u001b[49m\u001b[43mn_cluster\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m4\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43mmax_iteration\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m100\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     14\u001b[0m y \u001b[38;5;241m=\u001b[39m km\u001b[38;5;241m.\u001b[39mPredict(X)\n\u001b[0;32m     16\u001b[0m \u001b[38;5;66;03m# Uncomment to visualize\u001b[39;00m\n\u001b[0;32m     17\u001b[0m \u001b[38;5;66;03m# plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow')\u001b[39;00m\n\u001b[0;32m     18\u001b[0m \u001b[38;5;66;03m# plt.show()\u001b[39;00m\n",
      "\u001b[1;31mTypeError\u001b[0m: K_Mean.__init__() got an unexpected keyword argument 'n_cluster'"
     ]
    }
   ],
   "source": [
    "from sklearn.datasets import make_blobs\n",
    "import matplotlib.pyplot as plt\n",
    "from K_Mean_Algorithem import K_Mean\n",
    "\n",
    "# Define centroids and cluster standard deviation\n",
    "centroids = [(2, 2), (8, 3)]\n",
    "cluster_std = [1, 1]\n",
    "\n",
    "# Generate sample data\n",
    "X, y = make_blobs(n_samples=500, centers=centroids, random_state=2, n_features=2, cluster_std=cluster_std)\n",
    "\n",
    "# Initialize and use the K_Mean class\n",
    "km = K_Mean(n_cluster=4,max_iteration=100)\n",
    "y = km.Predict(X)\n",
    "\n",
    "# Uncomment to visualize\n",
    "# plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow')\n",
    "# plt.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
