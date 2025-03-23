# 1. Клонируем старый репозиторий
git clone https://github.com/msasmsasmsas/HSA13_hw22_profiling.git
cd HSA13_hw22_profiling

# 2. Переименовываем старый origin
git remote rename origin old-origin

# 3. Добавляем новый origin — на твой пустой проект
git remote add origin https://github.com/msasmsasmsas/HSA_hw23_ci_cd.git

# 4. Отправляем весь код и историю коммитов в новый репозиторий
git push -u origin --all
git push -u origin --all --force


# 5. Если в проекте были теги (релизы), отправляем их тоже
git push origin --tags
