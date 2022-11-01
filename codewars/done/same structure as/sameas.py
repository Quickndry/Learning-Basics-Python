import re
def same_structure_as(original, other):

    original_str = repr(original)

    other_str = repr(other)

    if '"' in original_str or '"' in other_str:
        original_ph = re.sub("\".+?\"", "", original_str)
        other_ph = re.sub("\".+?\"", "", other_str)
        original_leftover = re.sub("[^\[\]\,]", "", original_ph)
        other_leftover =  re.sub("[^\[\]\,]", "", other_ph) 

    elif "'" in original_str or "'" in other_str:
        original_ph = re.sub("\'.+?\'", "", original_str)
        other_ph = re.sub("\'.+?\'", "", other_str)
        original_leftover = re.sub("[^\[\]\,]", "", original_ph)
        other_leftover =  re.sub("[^\[\]\,]", "", other_ph)
        
    else:
        original_leftover = re.sub("[^\[\]\,]", "", original_str)
        other_leftover =  re.sub("[^\[\]\,]", "", other_str)

    if original_leftover == other_leftover:
        return True

    else:
        return False

