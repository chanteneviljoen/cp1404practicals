"""
CP1404/CP5632 Practical
Cleanup inconsistent song lyrics file names
Note: A complete solution for this exercise is NOT provided.
It's a very good thinking exercise and is less about the patterns we usually focus on
and more of a "tricky" problem to solve.
"""
import os
import shutil


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    # os.chdir('Lyrics')
    # for directory_name, subdirectories, filenames in os.walk('.'):
    # print("Directory:", directory_name)
    # print("\tcontains subdirectories:", subdirectories)
    # print("\tand files:", filenames)
    # print("(Current working directory is: {})".format(os.getcwd()))

    # for filename in filenames:
    #     new_name = get_fixed_filename(filename)
    #     print("Renaming {} to {}".format(filename, new_name))

    #     full_name = os.path.join(directory_name, filename)
    #     new_name = os.path.join(directory_name, new_name)
    #     os.rename(full_name, new_name)

    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # No solution is provided, but you may want to consider the patterns to look out for and fix
    # E.g. a lowercase letter followed by a capital, like "tN" should become "t_N"
    # Try doing this on paper first and then see if you can systematise it
    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    # return new_name
    filename_split = filename.split('.')
    f_name = '.'.join(filename_split[:-1])
    ext = '.' + filename_split[-1].lower()
    sections = []
    current_section = f_name[0]
    for char in f_name[1:]:
        if char.isspace() or char == '_':
            sections.append(current_section)
            current_section = ''
            continue
        elif char == ')':
            current_section += char
            sections.append(current_section)
            current_section = ''
            continue
        elif char.isupper() or char == '(':
            if len(current_section) == 0:
                current_section = char
                continue
            if current_section[-1] != '(':
                sections.append(current_section)
                current_section = char
                continue
        current_section += char
    if len(current_section) != 0:
        sections.append(current_section)

    return '_'.join(section.title() for section in sections) + ext


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            print('-')
            print(filename)
            print(get_fixed_filename(filename))
            full_path = os.path.join(directory_name, filename)
            new_path = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_path, new_path)


# demo_walk()
main()
