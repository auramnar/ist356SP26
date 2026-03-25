import pickle



# load data from a specified pickle file and return it.
# rb is read binary mode
def load_cache(pickle_file):
    '''
    open and deserialize a dictionary
    from the pickle file. If the file does not exist,
    returns an empty dictionary.
    '''
    
    try:
        with open(pickle_file, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
    
# clear the cache by overwriting the pickle file with an empty dictionary
#opens file in write binary mode ('wb'), overwrite the file contents (or create a file)
def clear_cache(pickle_file):
    '''
    opens pickle file in write-binary mode
    and replaces contents with an empty dictionary. If the file does
    not exist, it will be created.
       
    '''
    
    with open(pickle_file, 'wb') as f:
        pickle.dump({}, f)
        return {}
    
    
# store the cache dictionary into a specified pickle file
def save_cache(cache, pickle_file):
    '''
    serializes (writes) the dictionary to the
    specified pickle file using binary format. If the file already exists,
    it will be overwritten; otherwise, a new file will be created
    
    '''
    
    with open(pickle_file, 'wb') as f:
        pickle.dump(cache, f)

if __name__ == '__main__':
    cache = clear_cache('test.pkl') # delete file and reset to empty dictionary
    assert cache == {} # check that the cache is empty
    cache['test'] = 'test' # add a key-value pair
    save_cache(cache, 'test.pkl') # save dictionary to a file. Use pickle to serialize.
    cache = load_cache('test.pkl') # read the file, deserialize, assign to cache
    assert cache == {'test': 'test'} # confirm file is saved
    assert cache['test'] == 'test' # check that the key test returns the right value

