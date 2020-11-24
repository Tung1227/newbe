def A_Star_Search(tree, initialState, initialState_value, goalTest):
    frontier = {}
    explored = {}
    frontier.update({initialState: initialState_value})

    state_name = ""
    state_value_cost = 0
    state_cost = {initialState: 0}  #dict chứa giá trị đường đi của điểm đang xét đến nút gốc

    while len(frontier) > 0:
        min = 100
        
        print("frontier >>",frontier)

        for state in frontier:
            if min > frontier[state]:
                min = frontier[state]

        for state in frontier:
            if frontier[state] == min:
                state_name = state
                state_value_cost = min
                break

        del frontier[state_name]

        explored.update({state_name: state_value_cost})
        
        if goalTest == state_name:
            print(explored)
            return True
        
        tempState = tree[state_name] 
          
        for neighbour in tempState:
            tempState_value = tempState[neighbour]["value"] # giá trị điểm
            tempState_cost = tempState[neighbour]["cost"] + state_cost[state_name] # giá trị đường đi
            state_cost.update({neighbour: tempState[neighbour]["cost"] + state_cost[state_name]}) # cập nhật giá trị đường đi của điểm trên
            if neighbour not in dict(frontier, **explored):
                frontier.update({neighbour: tempState_value + tempState_cost})
            else: 
                if neighbour in dict(frontier,**explored):
                    if (tempState_value + tempState_cost) < dict(frontier, **explored)[neighbour]:
                        frontier.update({neighbour: tempState_value + tempState_cost})
    return False



if __name__ == "__main__":
    tree = {
        "A": {"B": {"value": 3, "cost": 2},
            "C": {"value": 4, "cost": 1},
            "D": {"value": 5, "cost": 3}},
        "B": {"E": {"value": 3, "cost": 5},
            "F": {"value": 1, "cost": 4},
            "A": {"value": 6, "cost": 2}},
        "C": {"G": {"value": 6, "cost": 6},
            "H": {"value": 2, "cost": 3},
            "A": {"value": 6, "cost": 1}},
        "D": {"I": {"value": 5, "cost": 2},
            "J": {"value": 4, "cost": 4},
            "A": {"value": 6, "cost": 3}},
        "E": {"B": {"value": 3, "cost": 5}},
        "F": {"K": {"value": 2, "cost": 2},
            "L": {"value": 0, "cost": 1},
            "M": {"value": 4, "cost": 4},
            "B": {"value": 3,"cost": 4}},
        "G": {"C": {"value": 4,"cost": 6}},
        "H": {"N": {"value": 0,"cost": 2},
            "O": {"value": 4,"cost": 4},
            "C": {"value": 4,"cost": 3}},
        "I": {"D": {"value": 5,"cost": 2}},
        "J": {"D": {"value": 5,"cost": 4}},
        "K": {"F": {"value": 1,"cost": 2}},
        "L": {"F": {"value": 1,"cost": 1}},
        "M": {"F": {"value": 1,"cost": 4}},
        "N": {"H": {"value": 2,"cost": 2}},
        "O": {"H": {"value": 2,"cost": 4}}
    }
    A_Star_Search(tree, "A", 6, "L")
