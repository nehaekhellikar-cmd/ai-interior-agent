def grade_design(action):
    if "modern" in action:
        return 10
    elif "luxury" in action:
        return 7
    elif "minimal" in action:
        return 5
    return 0
