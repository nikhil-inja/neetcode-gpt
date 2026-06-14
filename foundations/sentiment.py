import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        words = []
        for s in positive:
            words += s.split(' ')
        for n in negative:
            words += n.split(' ')
        words = list(sorted(set(words)))
        vocab = {}
        for i in range(len(words)):
            vocab[words[i]] = torch.Tensor([float(i + 1)])
        
        pos = []
        neg = []

        for p in positive:
            s = p.split(' ')
            sentence = []
            for w in s:
                sentence.append(vocab[w])
            pos.append(torch.Tensor(sentence))

        for n in negative:
            s = n.split(' ')
            sentence = []
            for w in s:
                sentence.append(vocab[w])
            neg.append(torch.Tensor(sentence))
        
        
        res = pos + neg

        res = nn.utils.rnn.pad_sequence(res, batch_first=True)

        return res
        
