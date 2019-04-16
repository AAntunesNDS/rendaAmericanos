import numpy as np

class Normalize:

    min_val = []
    max_val = []
    
    def fit(self, X):
        self.min_val = X.min(axis=0)
        self.max_val = X.max(axis=0)
    
    def transform(self, X):
        return (X - self.min_val) / (self.max_val - self.min_val)
    

class Standardize:
    
    def fit(self, X):
        self.mean = np.mean(X)
        self.std = np.std(X)
    
    def transform(self, X):           
        return (X - self.mean) / self.std