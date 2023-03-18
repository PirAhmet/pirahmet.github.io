def make_anchor_set():
    # Get the input strings from the user (20 inputs in total)
    input_strs = []
    for i in range(20):
        input_str = input() #(f"Enter the URLs and comments for input {i+1} separated by a space (one pair per line):\n")
        input_strs.append(input_str)

    # Split each input string into lines and remove any leading/trailing spaces
    lines_list = [[line.strip() for line in input_str.split('\n')] for input_str in input_strs]

    # Split each line into URL and comment and remove any leading/trailing spaces
    url_comments_list = [[line.split(' ', 1) for line in lines] for lines in lines_list]

    # Generate the HTML for each URL/comment pair
    anchors_list = [[f'<a href="{url}" title="{comment}">{url}</a>' for url, comment in url_comments] for url_comments in url_comments_list]

    # Combine the HTML for each pair into a single string with the appropriate index
    anchor_sets = ['\n'.join([f'{anchor} {idx}th elements' for idx, anchor in enumerate(anchors)]) for anchors in anchors_list]

    return '\n\n'.join(anchor_sets)



anchor_set = make_anchor_set()
print(anchor_set)

