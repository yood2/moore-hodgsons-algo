#include <iostream>
#include <vector>
#include <./pybind11/pybind11.h>

using namespace std;

class Task {
    public:
        string title;
        int duration;
        int due_time;
        Task(string title, int duration, int due_time) {
            this->title = title;
            this->duration = duration;
            this->due_time = due_time;
        }
        void print_details() {
            cout << "Title: " << this->title << ", Duration: " << this->duration << ", Due Time: " << this->due_time << endl;
        }
};

class Schedule {
    private:
        vector<Task> tasks;
    
    public:
        void addTask(const Task& task) {
            tasks.push_back(task);
        }

        void printSchedule() {
            for (const auto& task : tasks) {
                cout << task.title << endl;
            }
        }
};

// // testing
// int main() {
//     Task first_task = Task("test", 2, 4);
//     first_task.print_details();
//     return 0;
// };

PYBIND11_MODULE(schedule, m) {

}