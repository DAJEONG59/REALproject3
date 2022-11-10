from django.contrib import messages
from django.shortcuts import render, redirect

from diary.forms import MemoryForm, KeywordForm
from diary.models import KeywordPost,Memory


def memory_list(request):
    memory_qs = Memory.objects.all()  #.order_by("-id")
    return render(request, "diary/memory_list.html", {
        "memory_list": memory_qs,
    })


def memory_detail(request, pk):
    memory = Memory.objects.get(pk=pk)
    return render(request, "diary/memory_detail.html", {
        "memory": memory,
    })


def memory_new(request):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "일기를 생성했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm()

    return render(request, "diary/memory_form.html", {
        "form": form,
    })


def memory_edit(request, pk):
    memory = Memory.objects.get(pk=pk)

    if request.method == "POST":
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "메모리를 저장했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm(instance=memory)

    return render(request, "diary/memory_form.html", {
        "form": form,
    })


def memory_delete(request, pk):
    memory = Memory.objects.get(pk=pk)

    # delete memory
    if request.method == "POST":
        memory.delete()
        messages.success(request, "메모리를 삭제했습니다.")
        return redirect("/diary/")

    return render(request, "diary/memory_confirm_delete.html", {
        "memory": memory,
    })

def gallery(request):
    return render(request, "diary/gallery.html")

# ---------------------------------------------------------------------------------------------------
# keyword diary--------------------------------------------------------------------------------------

# 목록 페이지는 위와 같음. 갤러리 or 달력으로 보여줌.


# 상세페이지
def k_detail_page(request, pk):
    keyword_memory = KeywordPost.objects.get(pk=pk)
    return render(request, "diary/keyword_detail.html", {
        "keyword_post": keyword_memory,
    })



# 키워드로 일기쓰기 (생성)

def keyword_new(request):
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "일기를 생성했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = KeywordForm()

    return render(request, "diary/keyword_form.html", {
        "form": form,
    })


def key_edit(request, pk):
    memory = KeywordPost.objects.get(pk=pk)

    if request.method == "POST":
        form = KeywordForm(request.POST, instance=memory)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "메모리를 저장했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm(instance=memory)

    return render(request, "diary/memory_form.html", {
        "form": form,
    })


def key_delete(request, pk):
    memory = KeywordPost.objects.get(pk=pk)

    # delete memory
    if request.method == "POST":
        memory.delete()
        messages.success(request, "일기를 삭제했습니다.")
        return redirect("/diary/")

    return render(request, "diary/memory_confirm_delete.html", {
        "memory": memory,
    })

