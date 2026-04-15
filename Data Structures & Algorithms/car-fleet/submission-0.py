class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[i, j] for i,j in zip(position,speed)]
        cars.sort(reverse=True)
        #sort cars by postion largest/closest will be first
        stack = []
        carfleets = 0
        for car in cars:
            time = (target - car[0])/car[1]
            if not stack:
                stack.append(time)
                carfleets += 1
            else:
                if stack[-1] < time:
                    stack = []
                    stack.append(time)
                    carfleets +=1
        return carfleets



