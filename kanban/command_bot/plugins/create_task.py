# -*- coding: utf-8 -*-

import re

from ..bot import respond_to
from kanban.models import Project, Stage, Task

@respond_to('create task (.*) in stage (.*)', re.IGNORECASE)
def create_task(message, task_name, stage_name):

	response = {'update': False}
	user = message.body['user']
	project_id = message.body['project_id']
	project = Project.objects.get(id=project_id)
	stage = Stage.objects.get(project=project, title=stage_name)
	task, created = Task.objects.get_or_create(title=task_name, 
											   project=project, 
											   stage=stage,
											   creator=user)
	if created:
		response['update'] = True
		response['stage_title'] = stage.title
		response['task_title'] = task.title
		response['task_id'] = task.id

	return response
