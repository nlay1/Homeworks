def my_map(func, *sequences):
       result = []
       if len(sequences) > 0:
           minl = min(len(subseq) for subseq in sequences)
           for i in range(minl):
              result.append(func(*[subseq[i] for subseq in sequences]))
       return result


