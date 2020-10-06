from storage import Storage

def test_add():
    #try our add function to add new key
    st = Storage({'a': 1, 'b': 2})
    key = 'c'
    val = 3
    st = st.add(key, val)
    assert st.get(key) == val, "Value {} for the new key {} added unsuccessfully".format(val, key)
    
    #try our add function to add existing key
    existing_key = 'b'
    try:
        st = st.add(existing_key, val)
    except Exception:
        pass
    else:
        print("After adding existing key {} Exseption not Raised".format(existing_key))


def test_remove():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    rem = st.remove(key)
    assert rem is None, "Key {} is not removed".format(key)
    key = 'c'
    rem = st.remove(key)
    assert rem == "Key not exist", "Removing unexisting key provide wrong answer"

def test_set():
    st = Storage({'a': 1, 'b': 2})
    key, value = 'b', 3
    st.set(key, value)
    val = st.get(key)
    assert val == 3, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    st.set(key, value)
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
