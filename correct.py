import re
import os


def wag_fisch(str1, str2):
  len_str1, len_str2 = len(str1), len(str2)
  if len_str1 > len_str2:
      str1, str2 = str2, str1
      len_str1, len_str2 = len_str2, len_str1

  cur_row = range(len_str1 + 1)
  for i in range(1, len_str2 + 1):
      prev_row, cur_row = cur_row, [i] + [0] * len_str1
      for j in range(1, len_str1 + 1):
          add, delete, change = prev_row[j] + 1, cur_row[j-1] + 1, prev_row[j-1]
          if str1[j-1] != str2[i-1]:
              change += 1
          cur_row[j] = min(add, delete, change)

  return cur_row[len_str1]

def correct_command(input):
  
  command_list = os.environ["COMMANDS"].split()
  potential_commands = []
  diffs = []
  for command in command_list:
    diff = wag_fisch(input, command)
    potential_commands.append(command)
    diffs.append(diff)
  min_diff = min(diffs)
  cor_positions = []
  for pos,diff in enumerate(diffs):
    if(diff == min_diff):
        cor_positions.append({pos})
  cor_pos = str(cor_positions[0])
  cor_pos = int(re.sub("[^0-9^.]", "", cor_pos))
  return(potential_commands[cor_pos])