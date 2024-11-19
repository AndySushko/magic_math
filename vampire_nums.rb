def puts_vampire_nums(num)
  if num.to_s.size.even?  # проверяем четное ли кол-во разрядов

    # Переводим число в массив цифр
    digits_array = num.to_s.chars.map(&:to_i)
    # Перебираем все варианты расположения элементов в массиве
    nums_array = digits_array.permutation.to_a
    
    # Разделяем варианты на числа
    first_part = []
    second_part = []
    half = digits_array.length / 2
    for i in nums_array
      first_part << i[0..(half - 1)].join.to_i
      second_part << i[half..-1].join.to_i
    end

    common_arr = []
    first_part.each_with_index do |value, index|
      common_arr << value
      # Исключаем повторения
      if value * second_part[index] == num && !common_arr.include?(second_part[index])
        puts value.to_s + ' * ' + second_part[index].to_s + ' = ' + num.to_s
      end
    end
    
  end
end

# Exapmle:
# puts_vampire_nums 1260