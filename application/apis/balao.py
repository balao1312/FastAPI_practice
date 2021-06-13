from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def balao():
    return {
        'data': {
            'name': 'balao',
            'age': '38',
            'gender': 'male',
            'profession': 'todigong'
        }
    }
