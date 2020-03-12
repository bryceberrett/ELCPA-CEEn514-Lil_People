# from django.shortcuts import render
# from django.shortcuts import reverse
# from tethys_sdk.permissions import login_required
# from tethys_sdk.gizmos import Button

from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import MapView, Button
from tethys_sdk.gizmos import TextInput, DatePicker, SelectInput
from tethys_sdk.workspaces import app_workspace
from tethys_sdk.gizmos import DataTableView
from tethys_sdk.gizmos import MVDraw, MVView
from tethys_sdk.gizmos import MVLayer
@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    PProp_button = Button(
        display_text='Project Proposal',
        name='Project_Proposal_Button',
        icon='glyphicon glyphicon-plus',
        style='success',
        href=reverse('lil_people_elcpa:PProp'),
    )


    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button,
        'PProp_button' : PProp_button
    }

    return render(request, 'lil_people_elcpa/home.html', context)

@login_required()
def PProp(request):
    """
    Shows our project proposal
    """

    context = {}

    return render(request, 'lil_people_elcpa/PProp.html', context)

