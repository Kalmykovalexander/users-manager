from .models import Users, Groups, UsersGroups
from .forms import UserForm, GroupForm
from .serializers import UsersSerializer, GroupsSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# View for show all users
def users(request):
    users = Users.objects.all()
    return render(request, 'users.html', context={'users': users})

# View for show all groups
def groups(request):
    groups = Groups.objects.all()
    return render(request, 'groups.html', context={'groups': groups})

# View for add a new user
def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.user = request.user
            user = user_form.save()
            user.save()
            return redirect('users')
    user_form = UserForm()
    return render(request, 'add.html', context={'user_form': user_form})

# View for add a new group
def add_group(request):
    if request.method == 'POST':
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group = group_form.save(commit=False)
            group.user = request.user
            group = group_form.save()
            group.save()
            return redirect('groups')
    group_form = GroupForm()
    return render(request, 'add.html', context={'group_form': group_form})

# View for edit a user
def edit_user(request, user_id):
    user = Users.objects.get(id=user_id)
    user_form = UserForm(
        request.POST or None,
        instance=user
    )
    if not user_form.is_valid():
        return render(request, 'edit.html', {
            'user_form': user_form,
            'user': user,
        })
    user = user_form.save()
    return redirect('users')

# View for edit a group
def edit_group(request, group_id):
    group = Groups.objects.get(id=group_id)
    group_form = GroupForm(
        request.POST or None,
        instance=group
    )
    if not group_form.is_valid():
        return render(request, 'edit.html', {
            'group_form': group_form,
            'group': group,
        })
    group = group_form.save()
    return redirect('groups')

# View for delete a user
def delete_user(request, user_id):
    user = get_object_or_404(Users, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect('users')
    return render(request, "delete.html", context={'user': user})

# View for delete a group
def delete_group(request, group_id):
    group = get_object_or_404(Groups, id=group_id)
    # All users of this group
    users_group = UsersGroups.objects.filter(group=group)
    # Check if request user is in group
    for user in users_group:
        if request.user.id == group.user.id:
            if request.method == "POST":
                group.delete()
                return redirect('groups')
    return render(request, "delete.html", context={'group': group})


# Rest APIView for users
class UsersList(APIView):
    """
    List all USERS, or create a new USER.
    """
    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a USERS instance.
    """
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Rest APIView for groups
class GroupsList(APIView):
    """
    List all GROUPS, or create a new GROUP.
    """
    def get(self, request, format=None):
        groups = Groups.objects.all()
        serializer = GroupsSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupDetail(APIView):
    """
    Retrieve, update or delete a GROUPS instance.
    """
    def get_object(self, pk):
        try:
            return Groups.objects.get(pk=pk)
        except Groups.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupsSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupsSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        group = self.get_object(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







