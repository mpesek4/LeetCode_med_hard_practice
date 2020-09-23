
# This is a fun one, will def go back to optimize as my solution got kind of unwieldy because I was focused on the edge cases more than a simpler big picture idea
# instead of my approach of using a stack and manipulating the original array based on collisions, I think it might be better to have a separate array thatr will have our answer
# and add/remove to this array as we iterate over asteroids

def asteroidCollision(asteroids):
    n = len(asteroids)
    
    left_indices = []
    for i in range(n):
        if asteroids[i] < 0:
            left_indices.append(i)
    
    while len(left_indices) > 0:
        # curr_idx = left_indices.pop()
        curr_idx = left_indices[-1]
        l_idx = len(left_indices)-1

        ''' I use a stack with all the negative asteroid indices, we must always start with the negative asteroid that has no positive asteroids behind it,
        that is what we are doing in our while statement, afterwards the main algo has 3 cases; 
        
        case 1 is our else statement:  if 5 collides with -5 both asteroids explode, need to update
         all the indices bigger than current to be 2 less than before since we are manipulating the original array
         
         case 2 is our if statement: if -5 collides with a smaller positive number we replace the smaller one and update our indices above curr_idx by -1 because of the deletion
         
         case 3 is our elif: if -5 collides with a bigger one, we delete our negative asteroid and update the indices above to be one less because of the deletion
         
         '''

         # This loop is necessary because if an asteroid destroys a neighbor, but then is equal to its next neighbor, this could influence larger negative asteroids to the right

         # example: [2 , 2,-2 -2]     we must begin with our first -2, but after those are destroyed our array is [2,-2] since now another case happens where a double deletion will occur
         # we need to make sure we go back to our higher idx, it makes sense to keep a stack for this and always make sure we check for this case
        while len(left_indices) > 1 and left_indices[l_idx-1] == left_indices[l_idx]-1:
            l_idx-=1        
        curr_idx = left_indices[l_idx]    
        if curr_idx == 0:
            break
        del left_indices[l_idx]
        if len(left_indices) > 0 and left_indices[-1] == curr_idx-1:
            continue      
        if curr_idx == 0:
            return asteroids
        if abs(asteroids[curr_idx]) > asteroids[curr_idx-1]:
            asteroids[curr_idx-1] = asteroids[curr_idx]
            del asteroids[curr_idx]
            for idx, val in enumerate(left_indices):
                if val > curr_idx:
                    left_indices[idx]-=1 
            left_indices.append(curr_idx-1)
            left_indices.sort()
        elif abs(asteroids[curr_idx]) < asteroids[curr_idx-1]:
            del asteroids[curr_idx]
            for idx, val in enumerate(left_indices):
                if val > curr_idx:
                    left_indices[idx]-=1            
        else:
            for idx, val in enumerate(left_indices):
                if val > curr_idx:
                    left_indices[idx]-=2
            del asteroids[curr_idx]
            del asteroids[curr_idx-1]
    return asteroids