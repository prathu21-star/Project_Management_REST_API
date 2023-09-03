from rest_framework.views import APIView
from ProjectBoard.models import Boardmodel, TaskModel
from ProjectBoard.serializer import ProjectSerializer, TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

@api_view(['GET'])
def project_view(request):
    data = {'message': 'This is a response'}
    return Response(data)

class ProjectBoardBase(APIView):
    """ 
    A project board is a unit of delivery for a project. Each board will have a set of tasks assigned to a user.
    
    """
    
    def update_task_status(self, task_id, new_status):
        try:
            task = TaskModel.objects.get(id=task_id)
            task.status = new_status
            task.save()
            return True
        except TaskModel.DoesNotExist:
            return False

    def post(self, request, format=None):
        if 'user_id' in request.data:
            id = self.add_task(request)
            return Response({"id": id}, status=status.HTTP_201_CREATED)

        elif len(request.data) == 3:
            id = self.create_board(request)
            return Response({"id": id}, status=status.HTTP_201_CREATED)

        elif len(request.data) == 2:
            id = self.update_task_status(request.data['id'], request.data['status'])
            return Response("Updated Successfully")

        elif len(request.data) == 1:
            boards = self.list_boards(request.data['id'])
            return Response(boards)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        if pk is not None:
            self.close_board(pk)
            return Response("Updated Successfully")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # create a board
    def create_board(self, request, format=None):
        """
        :param request: A json string with the board details.
        {
            "name" : "<board_name>",
            "description" : "<description>",
            "team_id" : "<team id>"
            "creation_time" : "<date:time when board was created>"
        }
        :return: A json string with the response {"id" : "<board_id>"}

        Constraint:
         * board name must be unique for a team
         * board name can be max 64 characters
         * description can be max 128 characters
        """
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data.get('id')

    # ... (rest of your methods)
def export_board(self, request):
    board_id = request.data.get('id')
    
    try:
        board = Boardmodel.objects.get(id=board_id)
        tasks = TaskModel.objects.filter(board=board)
    except Boardmodel.DoesNotExist:
        return Response({"error": "Board not found"}, status=status.HTTP_404_NOT_FOUND)
    
    export_data = f"Board Name: {board.name}\n"
    export_data += f"Description: {board.description}\n\n"
    
    for task in tasks:
        export_data += f"Task: {task.title}\n"
        export_data += f"Status: {task.status}\n"
        export_data += f"Description: {task.description}\n\n"
    
    # Define the file name and path
    file_name = f"project_board_export.txt"
    file_path = os.path.join("out", file_name)
    
    # Write data to the text file
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create the directory if it doesn't exist
    with open(file_path, 'w') as file:
        file.write(export_data)
    
    return Response({"out_file": file_name}, status=status.HTTP_200_OK)