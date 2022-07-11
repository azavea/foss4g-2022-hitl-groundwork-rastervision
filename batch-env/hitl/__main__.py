import argparse

from hitl import loop

# def cli(annotation_project_id):
def cli():
    parser = argparse.ArgumentParser(description='Run HITL loop')
    parser.add_argument('annotation_project_ID',
                        metavar='ANNOTATION_PROJECT_ID',
                        help='Annotation project to to iterate')

    args = parser.parse_args()
    annotation_project_id = args.annotation_project_id
    # loop(annotation_project_id)
    loop()



if __name__ == "__main__":
    cli()
